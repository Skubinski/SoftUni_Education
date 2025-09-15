from collections import deque
bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
intelligence = int(input())
currently_used_bullets = 0
total_used_bullets = 0
while bullets:
    bullet = bullets.pop()
    if bullet <= locks[0]:
        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")
    currently_used_bullets += 1
    total_used_bullets += 1
    if currently_used_bullets == gun_barrel_size and bullets:
        currently_used_bullets = 0
        print("Reloading!")
    if not locks:
        print(f"{len(bullets)} bullets left. Earned ${intelligence - total_used_bullets * bullet_price}")
        break

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
