# -*- coding: utf-8 -*-
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

PIPELINE_CSS = {
    'sitterfied': {
        'source_filenames': (
            'css/style.css',
            'css/vendor/*.css',
            'css/vendor/font-awesome-4.0.3/css/font-awesome.min.css'
        ),
        'output_filename': 'css/sitterfied.css',
        'variant': 'datauri',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
}

PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.cssmin.CSSMinCompressor'

PIPELINE_JS = {
    'onboarding': {
        'source_filenames': (
            'js/lib/jquery-1.9.1.js',
            'js/lib/jquery.fancybox.pack.js',
            'js/lib/jquery-ui-1.10.0.custom.min.js',
            'js/lib/select2.js',
            'js/lib/uploadcare-0.15.0.min.js',
            'js/lib/jquery.form.min.js',
            'js/lib/jquery.formset.min.js',
            'js/lib/ie-popup.js',
            'js/facebook.js',

        ),
        'output_filename': 'js/libs.js',
    }
}

PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.slimit.SlimItCompressor'

PIPELINE_COMPILERS = (
    'pipeline.compilers.coffee.CoffeeScriptCompiler',
    'pipeline_compass.compiler.CompassCompiler',
)

#allow things to be global
PIPELINE_DISABLE_WRAPPER = True
