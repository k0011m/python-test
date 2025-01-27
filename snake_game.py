import time
import keyboard
import random

# ヘビの動き
class snake_move:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    #ヘビの向きによって座標を合わせてる
    def move(self, input_Direction):
        if input_Direction == None:
            pass
        elif input_Direction == 'right':
            self.x += 1
        elif input_Direction == 'left':
            self.x -= 1
        elif input_Direction == 'up':
            self.y += 1
        elif input_Direction == 'down':
            self.y -= 1
    
    def print_pos(self):
        print(self.x, self.y)
    
    def get_pos(self):
        return self.x, self.y

# マップ作成
class map:
    def __init__(self, r):
        self.r = r
        d_string = (r*2)*'〇'
        map_list = [d_string]*(r*2)
        print('\n'.join(map_list))


#main
if __name__ == "__main__":
    map_size = int(input('Press map size(r):'))
    map(map_size)
    snake_pos = snake_move(map_size, map_size)
    snake_dir = 'right'
    while True:
        time.sleep(0.5)
        if keyboard.is_pressed('w'):
            if snake_dir == 'down':
                break
            snake_dir = 'up'
        elif keyboard.is_pressed('s'):
            if snake_dir == 'up':
                break
            snake_dir = 'down'
        elif keyboard.is_pressed('a'):
            if snake_dir == 'right':
                break
            snake_dir = 'left'
        elif keyboard.is_pressed('d'):
            if snake_dir == 'left':
                break
            snake_dir = 'right'
        snake_pos.move(snake_dir)
        snake_x, snake_y = snake_pos.get_pos()
        if snake_x > map_size*2 or snake_y > map_size*2 or snake_x < 0 or snake_y < 0:
            print('Game Over!')
            break
        snake_pos.print_pos()