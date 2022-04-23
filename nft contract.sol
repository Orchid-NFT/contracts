// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract OrchidNFT is ERC1155, Ownable {
    string ipfsURI;
    uint lastMintedId;
    constructor() ERC1155("") {
        lastMintedId = 0;
    }

    function setURI(string memory newuri) public onlyOwner {
        ipfsURI = newuri;
        _setURI(newuri);
    }

    function getURI() public view returns(string memory){
        return ipfsURI;
    }

    function mint(address account, uint256 amount, bytes memory data)
        public
    {
        lastMintedId = lastMintedId+1;
        _mint(account, lastMintedId, amount, data);
        
    }

    function mintBatch(address to, uint256[] memory ids, uint256[] memory amounts, bytes memory data)
        public
        onlyOwner
    {
        _mintBatch(to, ids, amounts, data);
    }
}