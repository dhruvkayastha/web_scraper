from html.parser import HTMLParser
import wikipediaapi
import sys


class Parser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.inHead = False
        self.skipData = False
        self.skipHeaderList = {'history', 'references', 'further reading', 'external links', 'see also', 'controversy', 'notes', 'technique', 'profession', 'education', 'etymology', 'discoveries', 'philosophy', 'academia'} # insert h2 headers to avoid here
        self.skipDataLevel = 100 # level > this will be skipped
        self.currDataLevel = 0
        self.levels = [1]


    def handle_starttag(self, tag, attrs):
        if tag == 'h2':
            self.inHead = True
            if self.skipDataLevel >= 2:
                self.skipDataLevel = 100
            while self.levels[-1] >= 2:
                self.levels.pop()
            self.levels.append(2)
            # self.skipDataLevel = 2 
            # self.currDataLevel = 2
        elif tag == 'h3':
            self.inHead = True
            if self.skipDataLevel >= 3:
                self.skipDataLevel = 100
            while self.levels[-1] >= 3:
                self.levels.pop()
            self.levels.append(3)
        elif tag == 'h4':   
            self.inHead = True
            if self.skipDataLevel >= 4:
                self.skipDataLevel = 100
            while self.levels[-1] >= 4:
                self.levels.pop()
            self.levels.append(4)
        else:
            return

    def handle_endtag(self, tag):
        if tag == 'h2' or tag == 'h3' or tag == 'h4':
            self.inHead = False
            # self.levels.pop()
        return
        print("End tag  :", tag)

    def handle_data(self, data):
        if self.inHead:
            if data.lower() in self.skipHeaderList:
                self.skipDataLevel = self.levels[-1]
                return
            else:
                if self.skipDataLevel > self.levels[-1]:
                    print("**"+data+"**")
                return

        # print("---levels--", self.levels, self.skipDataLevel)

        if len(self.levels) == 0 or self.skipDataLevel <= self.levels[-1]:
            # if len(self.levels) != 0:
            #     self.levels.pop()
            return
        print(data,end=' ')

        return



wiki_html = wikipediaapi.Wikipedia(language='en', extract_format=wikipediaapi.ExtractFormat.HTML)


# pages = ['software_engineering', 'software_testing', 'software_design', 'software_development', 'Software_maintenance', 'software_requirements']
pages = ['computer_science', 'computer_programming', 'programming_paradigm', 'software_quality_assurance', 'object-oriented_programming', 'Systems_development_life_cycle']


for page_title in pages:

    sys.stdout = open('corpus/' + page_title + '.txt', 'w')

    page = wiki_html.page(page_title) # insert title here
    print('***'+page_title.replace('_', ' ')+'***')
    parser = Parser()
    # with open('page.html') as f:
    #     data = f.read()
    parser.feed(page.text)
