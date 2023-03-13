// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";


contract SimpleStorage {    
    uint256 favoriteNumber;
    address owner;
    address[] public funders;
    AggregatorV3Interface public priceFeed;

    constructor(address _priceFeed) public {
        priceFeed = AggregatorV3Interface(_priceFeed);
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
        require(
            (minimumUSD * 1e18) / getEthPrice() <= msg.value,
            "You need to spend more ETH mate!"
        );
        (bool success, ) = owner.call{value: msg.value}("");
        require(success, "Transfer failed.");
        funders.push(msg.sender);
    }

    function getFee() public view returns (uint256) {
        uint256 minimumUSD = 50;
        return (minimumUSD * 1e18) / getEthPrice();
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

    function getEthPrice() public view returns (uint256) {
        uint8 num_decimals = priceFeed.decimals();
        (, int256 answer, , , ) = priceFeed.latestRoundData();
        return uint256(answer / int256(10 ** num_decimals));
    }

    function getVersion() public view returns (uint256) {
        return priceFeed.version();
    }
}
