TARGETS=README.md

.PHONY: all clean

all: $(TARGETS)

clean:
	$(RM) -r doc/img $(TARGETS)

README.md: doc/README_plain.md ./md_replace_math.py
	$(RM) -r doc/img
	cat $< | python ./md_replace_math.py --imgdir doc/img > $@

