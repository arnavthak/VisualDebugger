import dearpygui.dearpygui as dpg
from BST import BST, BSTNode

start_circle = (500, 25)
#start_text = (143, 12)

def add_tuple(tuple1, tuple2):
    return tuple(sum(x) for x in zip(tuple1, tuple2))

def draw_subtree(node, circle):
    if not node:
        pass
    else:
        dpg.draw_circle(circle, 25, color=(255, 255, 255, 255))
        dpg.draw_text(add_tuple(circle, (-7, -13)), str(node.val), color=(250, 250, 250, 255), size=25)
        if node.left:
            #print("left exists")
            # dpg.draw_line((10, 10), (100, 100), color=(255, 0, 0, 255), thickness=1)
            dpg.draw_line(add_tuple(circle, (-20, 20)), add_tuple(circle, (-75, 75)), color=(255, 255, 255, 255), thickness=1)
            draw_subtree(node.left, add_tuple(circle, (-95, 95)))
        if node.right:
            #print("right exists")
            dpg.draw_line(add_tuple(circle, (20, 20)), add_tuple(circle, (75, 75)), color=(255, 255, 255, 255), thickness=1)
            draw_subtree(node.right, add_tuple(circle, (95, 95)))

def draw_BST(bst):
    dpg.create_context()
    dpg.create_viewport(title='Visual Debugger', width=1000, height=1000)

    with dpg.window(label="BST"):
        
        with dpg.drawlist(width=1000, height=1000):

            draw_subtree(bst.root, start_circle)
            
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == '__main__':
    bst = BST()
    bst.put(2)
    bst.put(1)
    bst.put(3)
    bst.put(-4)
    bst.put(17)
    bst.put(0)
    bst.put(9)
    bst.put(2.5)
    bst.put(2.75)

    # print(bst.root.val)
    # print(bst.root.left.val)
    # print(bst.root.right.val)

    draw_BST(bst)