from brownie import accounts, web3, interface, UsdcSTG, UsdtSTG

def main():
    chain = "fuji"
    token = "usdt"
    tokenInfo = {
        "goerli": {
            "usdc" :"0xdf0360ad8c5ccf25095aa97ee5f2785c8d848620",
            "usdt" :"0x5BCc22abEC37337630C0E0dd41D64fd86CaeE951",
            "stgToken" :"0xe0D6deF971250715Cb97794D4105CBf28f389BB8",
        },
        "fuji": {
            "usdc": "0x4A0D1092E9df255cf95D72834Ea9255132782318",
            "usdt": "0x134Dc38AE8C853D1aa2103d5047591acDAA16682",
            "stgToken": "0x1Cb74544AaafBA3350C0E1149DDb304Bb0A0ff61",
        },
        "initercmint": 10000000000000,
        "initstgmint": 6000000000000000000000000,
    }
    if token == "usdc":
        dexContract = UsdcSTG.deploy(tokenInfo[chain][token], tokenInfo[chain]["stgToken"], {"from": accounts.load("0")})
    if token == "usdt":
        dexContract = UsdtSTG.deploy(tokenInfo[chain][token], tokenInfo[chain]["stgToken"], {"from": accounts.load("0")})

    erc20Contract = interface.IERC20(tokenInfo[chain][token])
    stgContract = interface.IERC20(tokenInfo[chain]["stgToken"])

    erc20Contract.approve(dexContract.address, tokenInfo["initercmint"], {"from": accounts.load("0")})
    dexContract.mint(0, tokenInfo["initercmint"], {"from": accounts.load("0")})

    stgContract.approve(dexContract.address, tokenInfo["initstgmint"], {"from": accounts.load("0")})
    dexContract.mint(1, tokenInfo["initstgmint"], {"from": accounts.load("0")})