from pyiron_contrib import Project
pr = Project("demo")
randspg = pr.create.job.RandSpg("test")
randspg.run()
print(randspg.run())
