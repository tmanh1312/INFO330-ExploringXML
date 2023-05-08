<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<!-- The result of this stylesheet should be 384 Pokemon -->

<xsl:template match="type[position() != last()]"><xsl:value-of select="text()"/>, </xsl:template>
<xsl:template match="type[position() = last()]">
  <xsl:value-of select="text()"/>
</xsl:template>

<!--
  These rules will generate text output rather than text; these are useful for more easily
  figuring out if you got the "select" queries correct. Once you have that figured out,
  then update the HTML version of these rules below (and comment these out!) to see a nicely-
  formatted HTML file.
  -->

<!-- <xsl:template match="/pokedex">
Single type pokemon: <xsl:value-of select="count(pokemon[count(type) = 1])" />:

<xsl:apply-templates select="pokemon[count(type) = 1]" />
</xsl:template>

<xsl:template match="pokemon">
    <xsl:value-of select="./name" /> (<xsl:value-of select="@pokedexNumber" />): <xsl:value-of select="./@classification" /> | <xsl:value-of select="./type" /> |
</xsl:template>
 -->
 
<!--
  These rules will generate HTML output rather than text. This is to demonstrate
  the power of using XSLT to create pretty output from XML sources.
  -->

<xsl:template match="/pokedex">
  <html>
    <body>
      <h2>Single-type Pokemon</h2>
      Count: <xsl:value-of select="count(pokemon[count(type) = 1])" />
      <table border="1">
        <tr bgcolor="#9acd32">
          <th>Name</th>
          <th>Classification</th>
          <th>Type</th>
        </tr>
        <xsl:apply-templates select="pokemon[count(type) = 1]" />
      </table>
    </body>
  </html>
</xsl:template>

<xsl:template match="pokemon">
  <xsl:value-of select="./name" /> (<xsl:value-of select="@pokedexNumber" />): <xsl:value-of select="./@classification" /> | <xsl:apply-templates select="type" /> |
  <xsl:text>&#xA;</xsl:text>
</xsl:template>


</xsl:stylesheet>