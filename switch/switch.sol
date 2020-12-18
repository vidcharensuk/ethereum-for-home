// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.8.0;

contract ledswitch {
    bool switchValue;
    function getSwitch() public view returns (bool){
        return switchValue;
    }
    function setSwitch(bool value) public{
        switchValue = value;
    }
}
