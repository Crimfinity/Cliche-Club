

label sroutestart:
    call ss1 from _call_ss1
    return
label nroutestart:
    call ns1 from _call_ns1
    call ynas2 from _call_ynas2
    call ns2 
    call nh1 
    call nh2 
    call nh3 
    call trip
    call nh4 
    call std 
    call nfd 
    jump ccredits 
   
label yroutestart:
    call ys1 from _call_ys1
    call ynas2 from _call_ynas2_1
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc