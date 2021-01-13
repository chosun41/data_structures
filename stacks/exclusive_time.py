def exclusiveTime(N, logs):
    ans = [0] * N
    stack = []
    prev_time = 0

    for log in logs:
        fn, typ, time = log.split(':')
        fn, time = int(fn), int(time)

        if typ == 'start':
            if stack:
                ans[stack[-1]] += time - prev_time 
            stack.append(fn)
            prev_time = time
        else:
            ans[stack.pop()] += time - prev_time + 1
            prev_time = time + 1

    return ans

if __name__=='__main__':
    # time and space: O(n)
    print(exclusiveTime(N = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]))
    # 0 start 0,stack=[0],prev_time=0,ans=[0,0]
    # 1 start 2,stack=[0,1],prev_time=2,ans=[2,0]
    # 1 end 5,stack=[0],prev_time=6,ans=[2,4]
    # 0 end 6,stack=[],prev_time=7,ans=[3,4]
    print(exclusiveTime(N = 1, logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]))
    print(exclusiveTime(N = 2, logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]))