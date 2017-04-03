import LanguageSource
import Inserter
class Main(object):
    def __init__(self):
        self.source = LanguageSource.LanguageSource()
        self.inserter = Inserter.Inserter()
    def Run(self):
        self.inserter.Insert(self.source.Get())

if __name__ == "__main__":    
    m = Main()
    m.Run()

