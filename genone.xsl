<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<!-- "Find all generation-1 Pokemon" -->
<!-- The result of this stylesheet should be the Pokemon 1 - 151 in the Pokedex -->

<!--
  These rules will generate text output rather than text; these are useful for more easily
  figuring out if you got the "select" queries correct. Once you have that figured out,
  then update the HTML version of these rules below (and comment these out!) to see a nicely-
  formatted HTML file.

  Your job here is to write the correct XPath expressions for the "select"s below
  in order to pull back the correct XML nodes. In some of the other stylesheets, you will
  need to write the full "apply-templates" text yourself.
  -->
<!-- <xsl:template match="/pokedex">
    <xsl:apply-templates select="pokemon[number(@pokedexNumber) &lt;= 151]" />
</xsl:template>

<xsl:template match="pokemon">
    <xsl:value-of select="concat(name, ' (', @pokedexNumber )" />) | <xsl:value-of select="@classification" /> | 
</xsl:template> -->

<!--
  These rules will generate HTML output rather than text. This is to demonstrate
  the power of using XSLT to create pretty output from XML sources.
  Note that the HTML table expects each row to look something like

  Bulbasaur (1) | Seed Pokémon

  ... where the name and the parenthesized Pokedex number are in the first column.
  -->
  <!-- Find all generation-1 Pokemon -->
  <xsl:template match="/pokedex">
    <html>
      <body>
        <h2>Generation One Pokemon</h2>
        <table border="1">
          <tr bgcolor="#9acd32">
            <th>Name (Pokedex Number)</th>
            <th>Classification</th>
          </tr>
          <xsl:apply-templates select="pokemon[number(@pokedexNumber) &lt;= 151]" />
        </table>
      </body>
    </html>
  </xsl:template>

  <xsl:template match="pokemon">
      <xsl:value-of select="concat(name, ' (', @pokedexNumber )" />) | <xsl:value-of select="@classification" /> | 
      <xsl:text>&#xA;</xsl:text>
</xsl:template>


</xsl:stylesheet>
