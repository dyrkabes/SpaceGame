class Order:
    def __init__(self, target, remove_order):
        self.target = target
        #hassatr ubrat'
        if hasattr(target, "component_type"):
            self.component_type = target.component_type
        target.remove_order = remove_order


