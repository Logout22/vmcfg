BEGIN {
    found_line = 0;
    exit_status = 1;
}
{
    if (found_line == 0 &&
            match($0, /state\ *([A-Z]*)/, res) >= 0) {
        #print "state of NW device: '" res[1] "'";
        found_line = 1;
        if(res[1] != "DOWN") {
            exit_status = 0;
        }
    }
}

END {
    exit exit_status;
}

