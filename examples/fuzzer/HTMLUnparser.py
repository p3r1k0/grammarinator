# Generated by Grammarinator 17.5r

from itertools import chain
from grammarinator.runtime import *


def html_space_transformer(node):

    for child in node.children:
        html_space_transformer(child)

    if isinstance(node, UnparserRule):
        new_children = []
        for child in node.children:
            new_children.append(child)
            if child.name == 'htmlTagName' and child.right_sibling and child.right_sibling.name == 'htmlAttribute' \
                    or child.name == 'htmlAttribute' \
                    or isinstance(child, UnlexerRule) and child.src and child.src.endswith(('<script', '<style', '<?xml')):
                new_children.append(UnlexerRule(src=' '))
        node.children = new_children

    return node



import HTMLUnlexer
class HTMLUnparser(Grammarinator):

    def __init__(self, lexer):
        super(HTMLUnparser, self).__init__()
        self.lexer = lexer
        self.set_options()

    def set_options(self):
        self.options = dict(tokenVocab="HTMLLexer", dot="any_unicode_char")

    
    def endOfHtmlElement(self):
        pass
    def htmlDocument(self, *, max_depth=float('inf')):
        current = self.create_node(UnparserRule(name='htmlDocument'))
        if max_depth >= self.min_depths['quant_18']:
            for _ in self.zero_or_more(max_depth=max_depth):
                weights = self.depth_limited_weights([1, 1], self.min_depths['alt_6'], max_depth)
                choice = self.choice(weights)
                if choice == 0:
                    current += self.scriptlet(max_depth=max_depth - 1)
                elif choice == 1:
                    current += self.lexer.SEA_WS(max_depth=max_depth - 1)

        if max_depth >= self.min_depths['quant_19']:
            for _ in self.zero_or_one(max_depth=max_depth):
                current += self.xml(max_depth=max_depth - 1)

        if max_depth >= self.min_depths['quant_20']:
            for _ in self.zero_or_more(max_depth=max_depth):
                weights = self.depth_limited_weights([1, 1], self.min_depths['alt_7'], max_depth)
                choice = self.choice(weights)
                if choice == 0:
                    current += self.scriptlet(max_depth=max_depth - 1)
                elif choice == 1:
                    current += self.lexer.SEA_WS(max_depth=max_depth - 1)

        if max_depth >= self.min_depths['quant_21']:
            for _ in self.zero_or_one(max_depth=max_depth):
                current += self.dtd(max_depth=max_depth - 1)

        if max_depth >= self.min_depths['quant_22']:
            for _ in self.zero_or_more(max_depth=max_depth):
                weights = self.depth_limited_weights([1, 1], self.min_depths['alt_8'], max_depth)
                choice = self.choice(weights)
                if choice == 0:
                    current += self.scriptlet(max_depth=max_depth - 1)
                elif choice == 1:
                    current += self.lexer.SEA_WS(max_depth=max_depth - 1)

        if max_depth >= self.min_depths['quant_23']:
            for _ in self.zero_or_more(max_depth=max_depth):
                current += self.htmlElements(max_depth=max_depth - 1)

        return current

    def htmlElements(self, *, max_depth=float('inf')):
        current = self.create_node(UnparserRule(name='htmlElements'))
        if max_depth >= self.min_depths['quant_24']:
            for _ in self.zero_or_more(max_depth=max_depth):
                current += self.htmlMisc(max_depth=max_depth - 1)

        current += self.htmlElement(max_depth=max_depth - 1)
        if max_depth >= self.min_depths['quant_25']:
            for _ in self.zero_or_more(max_depth=max_depth):
                current += self.htmlMisc(max_depth=max_depth - 1)

        return current

    def htmlElement(self, *, max_depth=float('inf')):
        local_ctx = dict()
        current = self.create_node(UnparserRule(name='htmlElement'))
        weights = self.depth_limited_weights([1, 1, 1, 1, 1, 1], self.min_depths['alt_9'], max_depth)
        choice = self.choice(weights)
        if choice == 0:
            current += self.lexer.TAG_OPEN(max_depth=max_depth - 1)
            current += self.htmlTagName(max_depth=max_depth - 1)
            local_ctx['open_tag'] = current.last_child
            if max_depth >= self.min_depths['quant_26']:
                for _ in self.zero_or_more(max_depth=max_depth):
                    current += self.htmlAttribute(max_depth=max_depth - 1)

            current += self.lexer.TAG_CLOSE(max_depth=max_depth - 1)
            current += self.htmlContent(max_depth=max_depth - 1)
            current += self.lexer.TAG_OPEN(max_depth=max_depth - 1)
            current += self.lexer.TAG_SLASH(max_depth=max_depth - 1)
            current += self.htmlTagName(max_depth=max_depth - 1)
            current.last_child = local_ctx['open_tag'].deepcopy()
            current += self.lexer.TAG_CLOSE(max_depth=max_depth - 1)
            self.endOfHtmlElement()
        elif choice == 1:
            current += self.lexer.TAG_OPEN(max_depth=max_depth - 1)
            current += self.htmlTagName(max_depth=max_depth - 1)
            local_ctx['open_tag'] = current.last_child
            if max_depth >= self.min_depths['quant_27']:
                for _ in self.zero_or_more(max_depth=max_depth):
                    current += self.htmlAttribute(max_depth=max_depth - 1)

            current += self.lexer.TAG_SLASH_CLOSE(max_depth=max_depth - 1)
            self.endOfHtmlElement()
        elif choice == 2:
            current += self.lexer.TAG_OPEN(max_depth=max_depth - 1)
            current += self.htmlTagName(max_depth=max_depth - 1)
            local_ctx['open_tag'] = current.last_child
            if max_depth >= self.min_depths['quant_28']:
                for _ in self.zero_or_more(max_depth=max_depth):
                    current += self.htmlAttribute(max_depth=max_depth - 1)

            current += self.lexer.TAG_CLOSE(max_depth=max_depth - 1)
            self.endOfHtmlElement()
        elif choice == 3:
            current += self.scriptlet(max_depth=max_depth - 1)
        elif choice == 4:
            current += self.script(max_depth=max_depth - 1)
        elif choice == 5:
            current += self.style(max_depth=max_depth - 1)
        return current

    def htmlContent(self, *, max_depth=float('inf')):
        current = self.create_node(UnparserRule(name='htmlContent'))
        if max_depth >= self.min_depths['quant_29']:
            for _ in self.zero_or_one(max_depth=max_depth):
                current += self.htmlChardata(max_depth=max_depth - 1)

        if max_depth >= self.min_depths['quant_30']:
            for _ in self.zero_or_more(max_depth=max_depth):
                weights = self.depth_limited_weights([1, 1, 1], self.min_depths['alt_10'], max_depth)
                choice = self.choice(weights)
                if choice == 0:
                    current += self.htmlElement(max_depth=max_depth - 1)
                elif choice == 1:
                    current += self.xhtmlCDATA(max_depth=max_depth - 1)
                elif choice == 2:
                    current += self.htmlComment(max_depth=max_depth - 1)
                if max_depth >= self.min_depths['quant_31']:
                    for _ in self.zero_or_one(max_depth=max_depth):
                        current += self.htmlChardata(max_depth=max_depth - 1)


        return current

    def htmlAttribute(self, *, max_depth=float('inf')):
        local_ctx = dict()
        current = self.create_node(UnparserRule(name='htmlAttribute'))
        weights = self.depth_limited_weights([1, 1], self.min_depths['alt_11'], max_depth)
        choice = self.choice(weights)
        if choice == 0:
            current += self.htmlAttributeName(max_depth=max_depth - 1)
            local_ctx['attr_name'] = current.last_child
            current += self.lexer.TAG_EQUALS(max_depth=max_depth - 1)
            current += self.htmlAttributeValue(max_depth=max_depth - 1)
        elif choice == 1:
            current += self.htmlAttributeName(max_depth=max_depth - 1)
            local_ctx['attr_name'] = current.last_child
        return current

    def htmlAttributeName(self, *, max_depth=float('inf')):
        current = self.create_node(UnparserRule(name='htmlAttributeName'))
        current += self.lexer.TAG_NAME(max_depth=max_depth - 1)
        return current

    def htmlAttributeValue(self, *, max_depth=float('inf')):
        current = self.create_node(UnparserRule(name='htmlAttributeValue'))
        current += self.lexer.ATTVALUE_VALUE(max_depth=max_depth - 1)
        return current

    def htmlTagName(self, *, max_depth=float('inf')):
        current = self.create_node(UnparserRule(name='htmlTagName'))
        current += self.lexer.TAG_NAME(max_depth=max_depth - 1)
        return current

    def htmlChardata(self, *, max_depth=float('inf')):
        current = self.create_node(UnparserRule(name='htmlChardata'))
        weights = self.depth_limited_weights([1, 1], self.min_depths['alt_12'], max_depth)
        choice = self.choice(weights)
        if choice == 0:
            current += self.lexer.HTML_TEXT(max_depth=max_depth - 1)
        elif choice == 1:
            current += self.lexer.SEA_WS(max_depth=max_depth - 1)
        return current

    def htmlMisc(self, *, max_depth=float('inf')):
        current = self.create_node(UnparserRule(name='htmlMisc'))
        weights = self.depth_limited_weights([1, 1], self.min_depths['alt_13'], max_depth)
        choice = self.choice(weights)
        if choice == 0:
            current += self.htmlComment(max_depth=max_depth - 1)
        elif choice == 1:
            current += self.lexer.SEA_WS(max_depth=max_depth - 1)
        return current

    def htmlComment(self, *, max_depth=float('inf')):
        current = self.create_node(UnparserRule(name='htmlComment'))
        weights = self.depth_limited_weights([1, 1], self.min_depths['alt_14'], max_depth)
        choice = self.choice(weights)
        if choice == 0:
            current += self.lexer.HTML_COMMENT(max_depth=max_depth - 1)
        elif choice == 1:
            current += self.lexer.HTML_CONDITIONAL_COMMENT(max_depth=max_depth - 1)
        return current

    def xhtmlCDATA(self, *, max_depth=float('inf')):
        current = self.create_node(UnparserRule(name='xhtmlCDATA'))
        current += self.lexer.CDATA(max_depth=max_depth - 1)
        return current

    def dtd(self, *, max_depth=float('inf')):
        current = self.create_node(UnparserRule(name='dtd'))
        current += self.lexer.DTD(max_depth=max_depth - 1)
        return current

    def xml(self, *, max_depth=float('inf')):
        current = self.create_node(UnparserRule(name='xml'))
        current += self.lexer.XML_DECLARATION(max_depth=max_depth - 1)
        return current

    def scriptlet(self, *, max_depth=float('inf')):
        current = self.create_node(UnparserRule(name='scriptlet'))
        current += self.lexer.SCRIPTLET(max_depth=max_depth - 1)
        return current

    def script(self, *, max_depth=float('inf')):
        current = self.create_node(UnparserRule(name='script'))
        current += self.lexer.SCRIPT_OPEN(max_depth=max_depth - 1)
        weights = self.depth_limited_weights([1, 1], self.min_depths['alt_15'], max_depth)
        choice = self.choice(weights)
        if choice == 0:
            current += self.lexer.SCRIPT_BODY(max_depth=max_depth - 1)
        elif choice == 1:
            current += self.lexer.SCRIPT_SHORT_BODY(max_depth=max_depth - 1)
        return current

    def style(self, *, max_depth=float('inf')):
        current = self.create_node(UnparserRule(name='style'))
        current += self.lexer.STYLE_OPEN(max_depth=max_depth - 1)
        weights = self.depth_limited_weights([1, 1], self.min_depths['alt_16'], max_depth)
        choice = self.choice(weights)
        if choice == 0:
            current += self.lexer.STYLE_BODY(max_depth=max_depth - 1)
        elif choice == 1:
            current += self.lexer.STYLE_SHORT_BODY(max_depth=max_depth - 1)
        return current

    default_rule = htmlDocument

    min_depths = {
        'alt_10': [3, 2, 2],
        'alt_11': [4, 3],
        'alt_12': [1, 1],
        'alt_13': [2, 1],
        'alt_14': [1, 1],
        'alt_15': [1, 1],
        'alt_16': [1, 1],
        'alt_6': [2, 1],
        'alt_7': [2, 1],
        'alt_8': [2, 1],
        'alt_9': [3, 3, 3, 2, 2, 2],
        'dtd': 1,
        'htmlAttribute': 3,
        'htmlAttributeName': 2,
        'htmlAttributeValue': 3,
        'htmlChardata': 1,
        'htmlComment': 1,
        'htmlContent': 0,
        'htmlDocument': 0,
        'htmlElement': 2,
        'htmlElements': 3,
        'htmlMisc': 1,
        'htmlTagName': 2,
        'quant_18': 1,
        'quant_19': 2,
        'quant_20': 1,
        'quant_21': 2,
        'quant_22': 1,
        'quant_23': 4,
        'quant_24': 2,
        'quant_25': 2,
        'quant_26': 4,
        'quant_27': 4,
        'quant_28': 4,
        'quant_29': 2,
        'quant_30': 2,
        'quant_31': 2,
        'script': 1,
        'scriptlet': 1,
        'style': 1,
        'xhtmlCDATA': 1,
        'xml': 1,
    }

