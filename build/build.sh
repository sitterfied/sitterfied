pushd .
DIR="$( cd -P "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
OUTPUT_DIR=$DIR/../sitterfied/static_source/js/
cd $OUTPUT_DIR
python $DIR/../templates.py build
node $DIR/r.js -o app.build.js
java -jar $DIR/compiler.jar --js sitterfied.js --language_in ECMASCRIPT5 --js_output_file sitterfied-min.js
popd
