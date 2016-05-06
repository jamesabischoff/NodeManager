#watcher nodes detect changes to config files / ROS params

"""adds a watch on file [f] associated with node [n]"""
def add_watch(f,n):

"""restarts node [n] when file [f] changes"""
def on_change(f,n):

"""reload YAML file [f] via 'rosparam load f'"""
def reload(f):