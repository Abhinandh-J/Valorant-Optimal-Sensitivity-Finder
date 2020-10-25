 ###      VALORANT Optimal Sensitivity Finder       ###
### From the algorithm TenZ(Pro player) explained on his stream, I wrote this code which helps you find your perfect in-game
# sensitivity. According to him, the average EDPI of pro players is 280 so I have entered it as default but feel free to change it
# according to your play style. The only input data this code asks for is your mouse DPI.                

pros_edpi = 280
dpi = int(input("Enter your Mouse DPI: "))
mid = pros_edpi/dpi
high = mid*1.5
low = mid/2
mid = float("{:.2f}".format(mid))
high = float("{:.2f}".format(high))
low = float("{:.2f}".format(low))
print("In game Sensitivity range is:")
print(f"High: {high}")
print(f"Medium: {mid}")
print(f"Low: {low}")
print("Try all the 3 sensitivities in training mode for 10 minutes each")
final = False
while final == False:
    ask = input("Which sensitivity feels more comfortable? (Input the answer as  High or Low): ")
    if ask =="High":
        mid = (mid + high)/2
        mid = float("{:.3f}".format(mid))
        print(f"New sensitivity range is from {mid} to {high} ")
    else:
        mid = (low + mid)/2
        mid = float("{:.3f}".format(mid))
        print(f"New sensitivity range is from {low} to {mid} ")
    final = input("Is this sensitvity perfect for you?(Answer as Yes or No): ")
    if final =="Yes":
        final = True
    else:
        final = False


    