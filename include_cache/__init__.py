# A monkey patch for Django to cache which urlpattern was used to satifsy
# a resolve. By pushing that pattern to the front of the queue, we can
# avoid having Django loop through all the patterns.

from django.core import urlresolvers
from django.core.urlresolvers import ResolverMatch, Resolver404
from django.utils.encoding import smart_str

_url_pattern_cache = {}


def resolve(self, path):
    tried = []
    match = self.regex.search(path)
    if match:
        new_path = path[match.end():]
        patterns = self.url_patterns[:]
        hint = _url_pattern_cache.get(path)
        if hint:
            patterns.insert(0, hint)
        for pattern in patterns:
            try:
                sub_match = pattern.resolve(new_path)
            except Resolver404, e:
                sub_tried = e.args[0].get('tried')
                if sub_tried is not None:
                    tried.extend([[pattern] + t for t in sub_tried])
                else:
                    tried.append([pattern])
            else:
                if sub_match:
                    sub_match_dict = dict([(smart_str(k), v) for k, v
                                           in match.groupdict().items()])
                    sub_match_dict.update(self.default_kwargs)
                    for k, v in sub_match.kwargs.iteritems():
                        sub_match_dict[smart_str(k)] = v

                    if path not in _url_pattern_cache:
                        _url_pattern_cache[path] = pattern

                    return ResolverMatch(sub_match.func, sub_match.args,
                                         sub_match_dict, sub_match.url_name,
                                         self.app_name or sub_match.app_name,
                                         [self.namespace] +
                                         sub_match.namespaces)
                tried.append([pattern])
        raise Resolver404({'tried': tried, 'path': new_path})
    raise Resolver404({'path': path})


def patch():
    urlresolvers.RegexURLResolver.resolve = resolve
