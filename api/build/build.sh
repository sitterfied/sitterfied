CURRENT_DIR=$(pwd)
DIR=/opt/sitterfied
OUTPUT_DIR=$DIR/sitterfied/static_source/js/
cd $OUTPUT_DIR
python $DIR/templates.py build
node $DIR/build/r.js -o app.build.js
java -jar $DIR/build/compiler.jar --js sitterfied.js --language_in ECMASCRIPT5 --js_output_file sitterfied-min.js
cd $CURRENT_DIR
