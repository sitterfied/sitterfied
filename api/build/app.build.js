({
    //appDir: ".",
    baseUrl: ".",
    //dir: "../webapp-build",
    out: "sitterfied.js",
    //Comment out the optimize line if you want
    //the code minified by UglifyJS.
    optimize: "none",

    //CompilerOptions: "--language_in ECMASCRIPT5",
    waitSeconds: 200,

    //CompilerOptions: "--compilation_level ADVANCED_OPTIMIZATIONS",

    //Stub out the cs module after a build since
    //it will not be needed.
    // exclude: ['coffee-script'],
    // stubModules: ['cs', 'text'],
    normalizeDirDefines: 'all',
    findNestedDependencies: true,
    mainConfigFile: './main.js',
    name: "sitterfied",
    logLevel: 3,
    // modules: [
    //     {
    //         name: "main",
    //         exclude: ['coffee-script']
    //     }
    // ]
})
