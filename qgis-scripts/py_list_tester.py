import os

dems = [
"C:\\myworld\\cgis\\adkhistory\\cugir\\k41elu.dem",
"C:\\myworld\\cgis\\adkhistory\\cugir\\k42elu.dem",
"C:\\myworld\\cgis\\adkhistory\\cugir\\k43elu.dem",
"C:\\myworld\\cgis\\adkhistory\\cugir\\k44elu.dem",
"C:\\myworld\\cgis\\adkhistory\\cugir\\k45elu.dem",
"C:\\myworld\\cgis\\adkhistory\\cugir\\k46elu.dem",
"C:\\myworld\\cgis\\adkhistory\\cugir\\l41elu.dem",
"C:\\myworld\\cgis\\adkhistory\\cugir\\l42elu.dem",
"C:\\myworld\\cgis\\adkhistory\\cugir\\l43elu.dem",
"C:\\myworld\\cgis\\adkhistory\\cugir\\l44elu.dem",
"C:\\myworld\\cgis\\adkhistory\\cugir\\l45elu.dem",
"C:\\myworld\\cgis\\adkhistory\\cugir\\l46elu.dem",
"C:\\myworld\\cgis\\adkhistory\\cugir\\m41elu.dem",
"C:\\myworld\\cgis\\adkhistory\\cugir\\m42elu.dem",
"C:\\myworld\\cgis\\adkhistory\\cugir\\m43elu.dem",
"C:\\myworld\\cgis\\adkhistory\\cugir\\m44elu.dem",
"C:\\myworld\\cgis\\adkhistory\\cugir\\m45elu.dem"
]

for path in dems:
    print(os.path.basename(path))