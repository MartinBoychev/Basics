start_range = str(input())
end_range = str(input())

st_1 = int(start_range[0])
st_2 = int(start_range[1])
st_3 = int(start_range[2])
st_4 = int(start_range[3])

end_1 = int(end_range[0])
end_2 = int(end_range[1])
end_3 = int(end_range[2])
end_4 = int(end_range[3])

for i in range(st_1, end_1 + 1):
    for j in range(st_2, end_2 + 1):
        for k in range(st_3, end_3 + 1):
            for l in range(st_4, end_4 + 1):
                if i % 2 != 0 and j % 2 != 0 and k % 2 != 0 and l % 2 != 0:
                    print(f"{i}{j}{k}{l}", end=" ")

