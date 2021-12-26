# Quelques fonctions 

######################################################
#detachAllPackages permet d'enlever tous les packages#
######################################################
detachAllPackages <- function() {
  basic.packages.blank <-  c("stats", 
                             "graphics", 
                             "grDevices", 
                             "utils", 
                             "datasets", 
                             "methods", 
                             "base")
  basic.packages <- paste("package:", basic.packages.blank, sep = "")
  
  package.list <- search()[ifelse(unlist(gregexpr("package:", search())) == 1, 
                                  TRUE, 
                                  FALSE)]
  
  package.list <- setdiff(package.list, basic.packages)
  
  if (length(package.list) > 0)  for (package in package.list) {
    detach(package, character.only = TRUE)
    print(paste("package ", package, " detached", sep = ""))
  }
}


##################################################
#PackageFacile charge et/ou installe les packages#
##################################################
PackageFacile <- function(requiredPackages){
  #on charge où installe les librairies
  for(p in requiredPackages){
    if(!require(p,character.only = TRUE)) install.packages(p)
    library(p,character.only = TRUE)
  }
  
}

##########################################
#importAGS charge une fc d'une gdb ou shp#
##########################################

importAGS<- function (fc,gdb=path,whereclause= NULL) {
  fc <- arc.open(paste(gdb, fc, sep="/"))
  #info <- arc.shapeinfo(L93_Departements_gen3)
  if(is.null(whereclause)) {
    fc <- arc.select(fc)} else {
      fc <- arc.select(fc,where_clause=whereclause)
    }
  fc <- arc.data2sp(fc)
  return (fc)
}

########
#Not in#
########
'%ni%' <- function(x,y)!('%in%'(x,y))

############################
#fonction Plotly ou ggplot2#
############################
graphePlotly <- function (Plotly,plot,x=0.7,y=0.85) {
  if (Plotly == TRUE) {
    gp <- plotly_build(plot)
    #gp %>% layout(margin = m ) %>% layout(legend = list(x, y))
    gp
  } else {
    plot
  }
}


######################
#fonction ajout alpha#
######################

# addalpha()
addalpha <- function(colors, alpha=1.0) {
  r <- col2rgb(colors, alpha=T)
  # Apply alpha
  r[4,] <- alpha*255
  r <- r/255.0
  return(rgb(r[1,], r[2,], r[3,], r[4,]))
}

# colorRampPaletteAlpha()
colorRampPaletteAlpha <- function(colors, n=32, interpolate='linear') {
  # Create the color ramp normally
  cr <- colorRampPalette(colors, interpolate=interpolate)(n)
  # Find the alpha channel
  a <- col2rgb(colors, alpha=T)[4,]
  # Interpolate
	if (interpolate=='linear') {
		l <- approx(a, n=n)
	} else {
		l <- spline(a, n=n)
	}
	l$y[l$y > 255] <- 255 # Clamp if spline is > 255
	cr <- addalpha(cr, l$y/255.0)
	return(cr)
}


######################
#disjonctif complet  #
######################

factor2ind <- function(x, baseline){
  # Given a factor variable x, create an indicator matrix of  dimension
  # length(x) x (nlevels(x)-1) dropping the column  corresponding to the
  # baseline level (by default the rst level is used as  baseline).
  # Example:
  #  x = gl(4, 2, labels = LETTERS[1:4])
  #  factor2ind(x)
  #  factor2ind(x, ‘‘C’’)
  xname <- deparse(substitute(x))
  n <- length(x)
  x <- as.factor(x)
  
  if(!missing(baseline)) x <- relevel(x, baseline)
  X <- matrix(0, n, length(levels(x)))
  X[(1:n) + n*(unclass(x) - 1)] <- 1
  dimnames(X) <- list(names(x), paste(xname, levels(x),sep = ':'))
  return(X[,-1,drop = FALSE])
}

