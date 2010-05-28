### Author: Dag Wieers <dag$wieers,com>

class dstat_plugin(dstat):
    """
    Provide memory information related to the dstat process.

    The various values provide information about the memory usage of the
    dstat process. This plugin gives you the possibility to follow memory
    usage changes of dstat over time.
    """
    def __init__(self):
        self.name = 'dstat cpu'
        self.vars = ('user', 'system', 'total')
        self.type = 'd'
        self.width = 4
        self.scale = 100

    def extract(self):
        res = resource.getrusage(resource.RUSAGE_SELF)

        self.set2['user'] = float(res.ru_utime)
        self.set2['system'] = float(res.ru_stime)
        self.set2['total'] = float(res.ru_utime) + float(res.ru_stime)

        for name in self.vars:
            self.val[name] = (self.set2[name] - self.set1[name]) * 1000.0 / elapsed

        if step == op.delay:
            self.set1.update(self.set2)

# vim:ts=4:sw=4:et
