struct Group
{
  uint stabPoint;  // An index into the base for the point stabilized by this group's subgroup.
  OrbitTree orbitTree; // A tree to keep track of the orbit in our group of the point stabilized by our subgroup.
  TransversalSet transversalSet; // A set of coset representatives of this group's subgroup.
  GeneratorSet generatorSet; // A set of permutations generating this group.
  Group* subGroup; // A pointer to this group's subgroup, or null to mean the trivial group.

  Group( uint stabPoint )
  {
    this->stabPoint = stabPoint;
    subGroup = nullptr;
  }
};

// The given set of generators need not be a strong generating set.  It just needs to generate the group at the root of the chain.
Group* MakeStabChain( const GeneratorSet& generatorSet, uint* base )
{
  Group* group = new Group(0);
  for( generator in generatorSet )
    group->Extend( generator, base );
  return group;
}

// Extend the stabilizer chain rooted at this group with the given generator.
void Group::Extend( const Permutation& generator, uint* base )
{
  // This is the major optimization of Schreier-Sims.  Weed out redundant Schreier generators.
  if( IsMember( generator ) )
    return;

  // Our group just got bigger, but the stabilizer chain rooted at our subgroup is still the same.
  generatorSet.Add( generator );

  // Explore all new orbits we can reach with the addition of the new generator.
  // Note that if the tree was empty to begin with, the identity must be returned
  // in the set to satisfy a condition of Schreier's lemma.
  newTerritorySet = orbitTree.Grow( generator, base );

  // By the orbit-stabilizer theorem, the permutations in the returned set are
  // coset representatives of the cosets of our subgroup.
  for( permutation in newTerritorySet )
    transversalSet.Add( permutation );

  // We now apply Schreier's lemma to find new generators for our subgroup.
  // Some iterations of this loop are redundant, but we ignore that for simplicity.
  for( cosetRepresentative in transversalSet )
  {
    for( generator in generatorSet )
    {
      schreierGenerator = CalcSchreierGenerator( cosetRepresentative, generator );
      if( schreierGenerator.IsIdentity() )
        continue;
      
      if( !subGroup )
        subGroup = new Group( stabPoint + 1 );

      subGroup->Extend( schreierGenerator, base );
    }
  }
}
