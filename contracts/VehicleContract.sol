// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "@openzeppelin/contracts/access/Ownable.sol";


contract VehicleContract is Ownable {    
    uint256 minimumUSD = 50;
    mapping(address => uint256) public balances;
    address[] client_addresses;
    string[] client_requested;
    mapping(string => string) private ipfs_hashes;
    mapping(bytes32 => bool) request_status;
    AggregatorV3Interface public priceFeed;

    constructor(address _priceFeed) public {
        priceFeed = AggregatorV3Interface(_priceFeed);
    }

    function add_data_adr(string memory data_id, string memory data_adr) public {
        ipfs_hashes[data_id] = data_adr;
    }

    function get_data_adr(string memory data_id) public view returns (string memory) {
        return ipfs_hashes[data_id];
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

    function requestAccess(string memory data_adr) public {
        bytes32 k = keccak256(abi.encodePacked(msg.sender, data_adr));
        client_addresses.push(msg.sender);
        client_requested.push(data_adr);
        request_status[k] = false;
    }

    function requestAccessPay(string memory data_adr) public payable {
        require(
            (minimumUSD * 1e18) / getEthPrice() <= msg.value,
            "You need to spend more ETH mate!"
        );
        bytes32 k = keccak256(abi.encodePacked(msg.sender, data_adr));
        client_addresses.push(msg.sender);
        client_requested.push(data_adr);
        request_status[k] = false;
    }

    function getRequests() public returns (address[] memory, string[] memory) {
        return (client_addresses, client_requested);
    }

    function grantAccess(uint256 index) public {
        address new_adr = client_addresses[index];
        string memory new_str = client_requested[index];
        bytes32 k = keccak256(abi.encodePacked(new_adr, new_str));
        request_status[k] = true;
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
