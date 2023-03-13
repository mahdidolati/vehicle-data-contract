// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "@openzeppelin/contracts/access/Ownable.sol";


contract SimpleStorage is Ownable {    
    uint256 minimumUSD = 50;
    mapping(address => uint256) public balances;
    AggregatorV3Interface public priceFeed;

    constructor(address _priceFeed) public {
        priceFeed = AggregatorV3Interface(_priceFeed);
    }

    function deposit() public payable {
        require(
            (minimumUSD * 1e18) / getEthPrice() <= msg.value,
            "You need to spend more ETH mate!"
        );
        balances[msg.sender] = balances[msg.sender] + msg.value;
    }

    function getFee() public view returns (uint256) {
        uint256 minimumUSD = 50;
        return (minimumUSD * 1e18) / getEthPrice();
    }

    function charge(address _buyer) public {
        uint256 ethPrice = getEthPrice();
        require(
            (minimumUSD * 1e18) / ethPrice <= balances[_buyer],
            "You need to deposit more ETH mate!"
        );
        balances[_buyer] = balances[_buyer] - ((minimumUSD * 1e18) / ethPrice);
    }

    function withdraw() public payable onlyOwner {
        payable(msg.sender).transfer(address(this).balance);
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
