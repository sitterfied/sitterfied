run:
	@honcho -e .development start

bld:
	@sh build/build.sh

PHONY: bld run
