import "@nomiclabs/hardhat-waffle";
import "@tenderly/hardhat-tenderly";
import "dotenv/config";

const {
    TENDERLY_FORK_URL
} = process.env

export default {
  solidity: "0.8.4",
  networks: {
    "tenderly-fork": {
      url: "resp.data.simulation_fork.id",
           "http://api.tenderly.co/api/v1/account"
    },
  },
};
