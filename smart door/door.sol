pragma solidity >=0.4.0 <0.7.0;

contract ledswitch {
    uint door;
    uint uidSwitch;

    function setDoorStat(uint k) public{
        door = k;
    }

    function setUidSwitch(uint k) public{
        uidSwitch = k;
    }

    function getUidSwitch() public view returns(uint){
        return uidSwitch;
    }

    function getDoorStat() public view returns(uint){
        return door;
    }

}