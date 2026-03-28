const { Parser } = require('xml2js');

module.exports = class AnalyticsParser {
  constructor(data) {
    this.data = data;
  }

  parse() {
    return new Promise((resolve, reject) => {
      const parser = new Parser();
      parser.parseString(this.data, (err, result) => {
        if (err) return reject(err);
        return resolve(result);
      });
    });
  }
};

module.exports.Parser = Parser;