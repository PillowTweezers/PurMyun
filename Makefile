###### EDIT ##################### 
#Directory with ui and resource files
RESOURCE_DIR = gui/resources
 
#Directory for compiled resources
COMPILED_DIR = gui/ui
 
#UI files to compile
UI_FILES = mainwindow.ui participantdialog.ui teamcreationdialog.ui participantcreationdialog.ui teamwidget.ui \
participanttablewidget.ui gradedialog.ui

#Qt resource files to compile
RESOURCES = mainwindow.qrc participantstable.qrc window.qrc
 
#pyuic4 and pyrcc4 binaries
PYUIC = pyside6-uic
PYRCC = pyside6-rcc
 
#################################
# DO NOT EDIT FOLLOWING
 
COMPILED_UI = $(UI_FILES:%.ui=$(COMPILED_DIR)/ui_%.py)
COMPILED_RESOURCES = $(RESOURCES:%.qrc=$(COMPILED_DIR)/%_rc.py)
 
all : resources ui
 
resources : $(COMPILED_RESOURCES) 
 
ui : $(COMPILED_UI)
 
$(COMPILED_DIR)/ui_%.py : $(RESOURCE_DIR)/%.ui
	$(PYUIC) $< -o $@
 
$(COMPILED_DIR)/%_rc.py : $(RESOURCE_DIR)/%.qrc
	$(PYRCC) $< -o $@
 
clean : 
	$(RM) $(COMPILED_UI) $(COMPILED_RESOURCES) $(COMPILED_UI:.py=.pyc) $(COMPILED_RESOURCES:.py=.pyc)

run:
	mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
	current_dir := $(notdir $(patsubst %/,%,$(dir $(mkfile_path))))
