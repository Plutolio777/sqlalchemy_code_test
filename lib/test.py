from sqlalchemy.engine.default import DefaultDialect
from sqlalchemy.event import listens_for



print()
c = DefaultDialect
c.dispatch

ins = DefaultDialect()
ins.dispatch


# @listens_for(Engine, "do_execute")
# def test1():
#     return


@listens_for(ins, "do_execute")
def test2():
    return
