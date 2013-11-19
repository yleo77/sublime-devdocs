# Written by Vitor Britto (code@vitorbritto.com.br / vitorbritto.com.br)
# based on Stackoverflow Search Plugin by Eric Martel (emartel@gmail.com / www.ericmartel.com)

import sublime
import sublime_plugin

import subprocess
import webbrowser


def SearchFor(text):
    url = 'http://devdocs.io/#q=' + text.replace(' ', '%20')
    webbrowser.open_new_tab(url)


class DevDocsSearchSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        #for selection in self.view.sel():
            ## if the user didn't select anything, search the currently highlighted word
            #if selection.empty():
                #text = self.view.word(selection)

            #text = self.view.substr(selection)
            #SearchFor(text)

        # just search for the first selection word
        # if it's null, search for the word under the cursor 
        # 2013-11-19 added by yleo77
        selection = self.view.sel()[0]
        if len(selection) == 0:
            selection = self.view.word(selection)
        text = self.view.substr(selection)   
        SearchFor(text)

class DevDocsSearchFromInputCommand(sublime_plugin.WindowCommand):
    def run(self):
        # Get the search item
        self.window.show_input_panel('Search DevDocs for', '',
            self.on_done, self.on_change, self.on_cancel)

    def on_done(self, input):
        SearchFor(input)

    def on_change(self, input):
        pass

    def on_cancel(self):
        pass
