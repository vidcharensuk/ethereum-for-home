 
pragma solidity >=0.4.0 <0.7.0;

contract Sorter {
    event finish(uint size, uint signature);
    
    function sort(uint size, uint signature) public {
        uint[] memory data = new uint[](size);
        for (uint x = 0; x < data.length; x++) {
            data[x] = size-x;
        }
        quickSort(data, 0, data.length - 1);
        emit finish(size, signature);
    }
    
    function quickSort(uint[] memory arr, uint left, uint right) public {
        uint i = left;
        uint j = right;
        if (i == j) return;
        uint pivot = arr[left + (right - left) / 2];
        while (i <= j) {
            while (arr[i] < pivot) i++;
            while (pivot < arr[j]) j--;
            if (i <= j) {
                (arr[i], arr[j]) = (arr[j], arr[i]);
                i++;
                j--;
            }
        }
        if (left < j)
            quickSort(arr, left, j);
        if (i < right)
            quickSort(arr, i, right);
    }
}

