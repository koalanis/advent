#!/bin/bash

var_exists() {
    if [ -z $1 ]; then 
        return 1;
    else 
        return 0;
    fi
}

get_args() {
    while [[ "$1" ]]; do

        case $1 in
            "--arg") arg="Howdy"
        esac
        echo $1
        shift
    done
}

check_cmd_action() {
    case $1 in
        "list") action="list";;
        "add") action="add";;
    esac

    if var_exists "$action"; then
        echo "valid action"
    else
        echo "invalid action"
    fi
}

# echo "santa"
# echo "$@"

# get_args "$@"

# echo $arg


# check_cmd_action "$1"


# if var_exists "$EDITOR"; then
#     echo "EDITOR exists";
# else
#     echo "EDITOR doesnt exist"
# fi

# if var_exists "$HOME"; then
#     echo "HOME exists";
# else
#     echo "HOME doesnt exist"
# fi

SANTA_SPLASH="santa - an advent of code utility"

SANTA_HELP_CONTENT=$(cat <<EOF
ex: santa [ACTION] [...ARGS]\n
commands \n
--------\n
check\t\tChecks for existance of an advent directory for a particular configuration\n
\t\t\tex: santa check 2015 -> checks if \$ADVENT_DIR/2015 directory is created\n
\t\t\tex: santa check 2016 java -> checks if \$ADVENT_DIR/2016/java\n
\t\t\tex: santa check 2016 java 12 -> checks if \$ADVENT_DIR/2016/java/12\n
EOF
)


print_help() {
    echo -e $SANTA_SPLASH
    echo -e $SANTA_HELP_CONTENT
}

check_if_advent_folder_exists() {
    return $(var_exists "$ADVENT_HOME")
}

check_advent_folder() {
    if check_if_advent_folder_exists; then
        echo "ADVENT HOME SET at $ADVENT_HOME"
    else
        echo "ADVENT HOME NOT SET"
    fi
}

print_no_action() {
    echo "$1 is not a valid action. Try santa help to learn more"
}

valid_year() {
    if [ "$1" -ge 2015 ]&& [ "$1" -le 2022 ]; then
        return 0
    fi
    return 1
}

check_directory() {
    prob_path="$ADVENT_HOME"
    while [[ "$1" ]]; do
        prob_path="$prob_path/$1"
        shift
    done
    if [[ -d $prob_path ]]; then
        return 0
    fi
    return 1
}

valid_lang() {
    if [ "$1"  == "data" ]; then
        return 1
    fi
    return 0
}

valid_day() {
    if [ "$1" -ge 1 ]&& [ "$1" -le 25 ]; then
        return 0
    fi
    return 1
}

handle_check() {

    if ! check_if_advent_folder_exists; then
        echo "\$ADVENT_HOME is not set"
        return 1
    fi

    year=$1
    if ! valid_year "$year"; then
        echo "$year is not valid"
        return 1
    fi

    if ! var_exists "$2"; then 
        check_directory "$year"
        out=$?
        if $out; then
            echo "Directory exists for Advent Year = $year"
        else
            echo "Directory for Advent Year = $year does NOT exist"
        fi
        return $out
    fi

    lang=$2
    if ! valid_lang "$lang"; then
        echo "$lang is not valid"
        return 1
    fi

    
    if ! var_exists "$3"; then 
        check_directory "$year" "$lang"
        out=$?
        if $out; then
            echo "Directory exists for Advent Year = $year and Language = $lang"
        else
            echo "Directory for Advent Year = $year and Language = $lang does NOT exist"
        fi
        return $out
    fi

    day=$3
    if ! valid_day "$day"; then
        echo "$day is not valid"
        return 1
    fi

    check_directory "$year" "$lang" "day$day"
    out=$?

    if [ $out -eq 0 ]; then
        echo "Directory exists for Advent Year = $year, Language = $lang and Day = $day"
    else
        echo "Directory for Advent Year = $year, Language = $lang and Day = $day does NOT exist"
    fi

    return $out
}

check_action() {
    case $1 in 
        check)
            shift
            handle_check "$@";;
        help)
            print_help;;
        *)
            print_no_action $1
    esac
    return $?
}



main() {

    check_action "$@"
    out=$?
    return $out
}

main "$@"
exit $?
