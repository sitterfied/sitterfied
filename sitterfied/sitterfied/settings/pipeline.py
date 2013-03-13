STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

PIPELINE_CSS = {
    'comingsoon': {
        'source_filenames': (
          'css/comingsoon.css',
          'css/vendor/*.css',

        ),
        'output_filename': 'css/comingsoon.css',
        'variant': 'datauri',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
    'sitterfied': {
        'source_filenames': (
          'css/sitterfied.css',
          'css/vendor/*.css',
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
    'app': {
        'source_filenames': (
            'js/jquery-1.9.0.min.js',
            'js/*.js',
            ),
        'output_filename': 'js/app.js',
    }
}
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.slimit.SlimItCompressor'

PIPELINE_COMPILERS = (
  'pipeline.compilers.coffee.CoffeeScriptCompiler',
  'pipeline_compass.compiler.CompassCompiler',
)
