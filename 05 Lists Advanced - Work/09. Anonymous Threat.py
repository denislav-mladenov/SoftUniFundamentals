data = input().split()

while True:
    command = input().split()
    if command[0] == "3:1":
        break
    elif command[0] == "merge":
        start = int(command[1])
        end = int(command[2])
        start = max(start, 0)
        end = min(end, len(data)-1)
        merged = ''.join(data[start:end+1])
        del data[start:end+1]
        data.insert(start, merged)
    elif command[0] == "divide":
        index = int(command[1])
        partitions = int(command[2])
        string = data[index]
        substring_length = len(string) // partitions
        result = [string[i:i+substring_length] for i in range(0, len(string), substring_length)]
        if len(result) < partitions:
            last_index = len(result) - 1
            while len(result) < partitions:
                result[last_index] += result.pop(last_index+1)
        data.pop(index)
        data[index:index] = result

print(' '.join(data))
