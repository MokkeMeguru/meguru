# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1520107020.4931772
_enable_loop = True
_template_filename = 'themes/yesplease/templates/_footer.tmpl'
_template_uri = '_footer.tmpl'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        content_footer = context.get('content_footer', UNDEFINED)
        template_hooks = context.get('template_hooks', UNDEFINED)
        __M_writer = context.writer()
        if content_footer:
            __M_writer('  <div class="yp-footer">\n    ')
            __M_writer(str(content_footer))
            __M_writer('\n    ')
            __M_writer(str(template_hooks['page_footer']()))
            __M_writer('\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/yesplease/templates/_footer.tmpl", "source_encoding": "ascii", "line_map": {"16": 0, "34": 28, "23": 1, "24": 2, "25": 3, "26": 3, "27": 4, "28": 4}, "uri": "_footer.tmpl"}
__M_END_METADATA
"""
