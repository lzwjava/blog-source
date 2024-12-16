.PHONY: awesome-cv

CC = xelatex
EXAMPLES_DIR = awesome-cv
RESUME_DIR = awesome-cv/resume
RESUME_ZH_DIR = awesome-cv/resume-zh
COVER_LETTER_DIR = awesome-cv/coverletter
RESUME_SRCS = $(shell find $(RESUME_DIR) -name '*.tex')
RESUME_ZH_SRCS = $(shell find $(RESUME_ZH_DIR) -name '*.tex')

awesome-cv: $(foreach x, coverletter coverletter-zh resume-zh resume, $x.pdf)

resume.pdf: $(EXAMPLES_DIR)/resume.tex $(RESUME_SRCS)
	$(CC) -output-directory=$(EXAMPLES_DIR) $<

resume-zh.pdf: $(EXAMPLES_DIR)/resume-zh.tex $(RESUME_ZH_SRCS)
	$(CC) -output-directory=$(EXAMPLES_DIR) $<

coverletter.pdf: $(COVER_LETTER_DIR)/coverletter.tex
	$(CC) -output-directory=$(COVER_LETTER_DIR) $<

coverletter-zh.pdf: $(COVER_LETTER_DIR)/coverletter-zh.tex
	$(CC) -output-directory=$(COVER_LETTER_DIR) $<

clean:
	rm -rf $(EXAMPLES_DIR)/*.pdf

copy:
	./update-resume.sh

