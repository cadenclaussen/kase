class Kase:
    def camel(self, input):
        k = input.split("_")
        w = ""
        w += k[0]
        for index in range(len(k)):
            if index == 0:
                continue
            w += (k[index]).capitalize()
        return w

    def snake(self, input):
        return input

    def Camel(self, input):
        k = input.split("_")
        w = ""
        for index in range(len(k)):
            w += (k[index]).capitalize()
        return w

    def Space(self, input):
        k = input.split("_")
        w = ""
        for index in range(len(k)):
            w += (k[index]).capitalize()
            w += " "
        return w

    def space(self, input):
        k = input.split("_")
        w = ""
        for index in range(len(k)):
            w += (k[index])
            w += " "
        return w

             