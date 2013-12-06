import os
import time
import sys

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

modules = ['sitterfied']

thisdir = os.path.dirname(os.path.realpath(__file__))
module_dirs =  [os.path.join(thisdir, mod, "static_source", "js", "templates") for mod in modules]

import fnmatch
import os

def safe_list_get (l, idx, default):
  try:
    return l[idx]
  except IndexError:
    return default

def compile_templates():
    print "compiling templates..."
    for template_dir in module_dirs:
        #html_files = os.path.join(template_dir "*.html")
        all_files = []
        for root, dirnames, filenames in os.walk(template_dir):
            for filename in fnmatch.filter(filenames, '*.hbs'):
                if "#" in filename:
                    continue
                all_files.append(os.path.join(root, filename))

        dest_path = os.path.join(template_dir,  "..", "templates.js")

        print "compiling ", template_dir
        print all_files
        os.system("ember-precompile %s -f %s" % (" ".join(all_files), dest_path))
        print "compiled ", template_dir
        with open(dest_path, 'r+') as fsock:
            content = fsock.read()
            fsock.seek(0)
            fsock.write("define(['ember'], function(Ember){")
            fsock.write(content)
            fsock.write('})')

        #os.system("rm %s" % (html_dir))


class Compiler(FileSystemEventHandler):
    def on_any_event(self, event):
        compile_templates()


if __name__ == "__main__":
    compile_templates()
    if safe_list_get(sys.argv, 1, 'watch') is 'watch':
        observer = Observer()
        compiler = Compiler()
        print module_dirs
        for module_dir in module_dirs:
            for root, dirnames, filenames in os.walk(module_dir):
                for dirname in dirnames:
                    dir = os.path.join(root, dirname)
                    observer.schedule(compiler, dir)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
