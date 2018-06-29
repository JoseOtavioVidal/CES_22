class Component(object):
    def __init__(self, *args, **kw):
        pass

    def component_function(self):
        pass


class Head(Component):
    def __init__(self, *args, **kw):
        Component.__init__(self, *args, **kw)

    def component_function(self):
        print("Thinking about the semester and trace a strategy to survey")

class Body(Component):
    def __init__(self, *args, **kw):
        Component.__init__(self, *args, **kw)

    def component_function(self):
        print("With my strategy, i will start right now")

class Composite(Component):
    def __init__(self, *args, **kw):
        Component.__init__(self, *args, **kw)
        self.children = []

    def append_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def get_child(self, index):
        if index < len(self.children):
            self.children[index].component_function()
        else:
            print("This object don't have so many components")

    def component_function(self):
        map(lambda x: x.component_function(), self.children)

class CompositeIntarface():
    def __init__(self, c):
        pass

    def call_the_components(self, index):
        c.get_child(index)



if __name__ == "__main__":
    c = Composite()
    head = Head()
    body = Body()
    c.append_child(head)
    c.append_child(body)
    c.component_function()
    interface = CompositeIntarface(c)
    interface.call_the_components(2)
    interface.call_the_components(0)