import time
import keyboard
import random
import subprocess

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
            self.y -= 1
        elif input_Direction == 'down':
            self.y += 1
    
    def print_pos(self):
        print(self.x, self.y)
    
    def get_pos(self):
        return self.x, self.y

class apple:

    def __init__(self, x, y):
        self.apple_x = x
        self.apple_y = y
        
    def get_apple_pos(self):
        return self.apple_x, self.apple_y
    
    def random_apple(self):
        self.apple_x = random.randint(0, map_size*2 - 1)
        self.apple_y = random.randint(0, map_size*2 - 1)
        while True:
            if not (self.apple_x, self.apple_y) == (snake_x, snake_y):
                break
            else:
                self.apple_x = random.randint(0, map_size*2 - 1)
                self.apple_y = random.randint(0, map_size*2 - 1)


# マップ作成
class map:
    def __init__(self, r):
        self.r = r
        self.d_string = (r*2)*'〇'
        self.map_list_reset = [self.d_string]*(r*2)
        #print('\n'.join(self.map_list))

    # マップの更新
    def map_update(self, x, y, apple_x_map, apple_y_map):
        global score
        #マップのリストを入手
        self.map_list = list(self.map_list_reset)
        if (x,y) == (apple_x_map, apple_y_map):
            score += 1
            poison_apple.append((apple_x_map,apple_y_map))
            apple_pos.random_apple()
        #ヘビのy座標とリンゴのy座標が同じときの文字列を取得
        if y == apple_y_map:
            x_string = self.map_list[int(y)]
            x_string = list(x_string)
            x_string[int(x)] = skin
            x_string[int(apple_x_map)] = '🍎'
            x_string = ''.join(x_string)
            self.map_list[int(y)] = x_string
        else:
            #ヘビのy座標とリンゴのy座標が違うときの文字列を取得
            try:
                x_string = self.map_list[int(y)]
                apple_x_string = self.map_list[int(apple_y)]
            except IndexError:
                print(f'Game Over!\nscore:{score}')
                exit()
            x_string = list(x_string)
            apple_x_string = list(apple_x_string)
        #x座標の文字列を更新
            try:
                x_string[int(x)] = skin
                apple_x_string[int(apple_x_map)] = '🍎'
            except IndexError:
                print(f'Game Over!\nscore:{score}')
                exit()
            x_string = ''.join(x_string)
            apple_x_string = ''.join(apple_x_string)
            self.map_list[int(y)] = x_string
            self.map_list[int(apple_y_map)] = apple_x_string
        self.map_list = '\n'.join(self.map_list)
        #マップを文字列にして、表示
        print(self.map_list,'\n\n\n\n')
        #マップの変数をリセット
        self.map_list = self.map_list_reset



def character():
    while True:
        character = input('Press character:')
        if len(character) == 1:
            return character
        else:
            print('Please enter one character.')

#main
if __name__ == "__main__":
    score = 0
    map_size = int(input('Press map size(r):'))
    skin = character()

    map_var = map(map_size)

    snake_pos = snake_move(map_size, map_size)
    snake_dir = 'right'

    poison_apple = []
    #map_var.map_update(5,4)
    apple_pos = apple(3,3)
    while True:
        time.sleep(0.2)
        if keyboard.is_pressed('w'):
            if not snake_dir == 'down':
                snake_dir = 'up'
        elif keyboard.is_pressed('s'):
            if not snake_dir == 'up':
                snake_dir = 'down'
        elif keyboard.is_pressed('a'):
            if not snake_dir == 'right':
                snake_dir = 'left'
        elif keyboard.is_pressed('d'):
            if not snake_dir == 'left':
                snake_dir = 'right'
        snake_pos.move(snake_dir)
        snake_x, snake_y = snake_pos.get_pos()
        if snake_x > map_size*2 or snake_y > map_size*2 or snake_x < 0 or snake_y < 0:
            print(f'Game Over!\nscore:{score}')
            break
        apple_x, apple_y = apple_pos.get_apple_pos()
        map_var.map_update(snake_x, snake_y,apple_x, apple_y)
        #map(map_size)