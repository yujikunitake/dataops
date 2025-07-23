db.Carros.aggregate([
  {
    $lookup: {
      from: "Montadoras",
      localField: "Montadora",
      foreignField: "Montadora",
      as: "MontadoraInfo"
    }
  },
  { $unwind: "$MontadoraInfo" },
  {
    $group: {
      _id: "$MontadoraInfo.País",
      Carros: {
        $push: {
          Carro: "$Carro",
          Cor: "$Cor",
          Montadora: "$Montadora"
        }
      }
    }
  },
  {
    $project: {
      _id: 0,
      País: "$_id",
      Carros: 1
    }
  }
]);
