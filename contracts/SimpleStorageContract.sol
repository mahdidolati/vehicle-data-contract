// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;


contract SimpleStorage {    
    uint256 favoriteNumber;
    address owner;
    address[] public funders;

    constructor() public {
        owner = msg.sender;
    }

    struct People {
        uint256 favoriteNumber;
        string name;
    }

    People[] public people;
    mapping(string => uint256) public nameToFavoriteNumber;

    receive() external payable {
        (bool s,) = payable(owner).call{value: msg.value}(new bytes(0));
        require(s);
    }

    function fund() public payable {
        uint256 minimumUSD = 50;
        uint256 usdWeiPrice = 50735;
        uint256 inUsd = msg.value / usdWeiPrice;
        require(
            inUsd >= minimumUSD,
            "You need to spend more ETH mate!"
        );
        (bool success, ) = owner.call{value: msg.value}("");
        require(success, "Transfer failed.");
        funders.push(msg.sender);
    }

    function store(uint256 _favoriteNumber) public {
        favoriteNumber = _favoriteNumber;
    }

    function retrieve() public view returns (uint256) {
        return favoriteNumber;
    }

    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        people.push(People(_favoriteNumber, _name));
        nameToFavoriteNumber[_name] = _favoriteNumber;
    }
}
