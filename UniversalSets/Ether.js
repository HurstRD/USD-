const {	TENDERLY_JSON_RPC_URL } = process.env

const provider = new ethers.providers.JsonRpcProvider(TENDERLY_JSON_RPC_URL);

const contract = new ethers.Contract(contractAddress;, contractABI, provider){

const unsignedTx = await contract.populateTransaction[funcName](...args)

const transactionParameters = [{

    to: contract.address,

    from: sender,

    data: unsignedTx.data,

    gas: ethers.utils.hexValue(300000),

    gasPrice: ethers.utils.hexValue(1),

    value: ethers.utils.hexValue(0)

}];

const txHash = await provider.send('eth_sendTransaction', transactionParameters)
